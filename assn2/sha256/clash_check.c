#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <openssl/sha.h>
#include <time.h>
#include <pthread.h>

#define DIGEST_LENGTH 32

#define NUM_THREADS 16
#define NUM_REPS 1
#define NUM_BITS_TO_MATCH 56

#define TABLE_SIZE 536870912ULL 
#define TABLE_MASK (TABLE_SIZE - 1)
#define EMPTY_HASH 0xFFFFFFFFFFFFFFFFULL

typedef unsigned __int128 uint128_t;

const char *suffix = "@iitk.ac.in";
size_t suffix_len;
const int prefix_len = 7;

uint128_t *hash_table;

int iter = 0;
volatile int found_flag = 0;

uint64_t winner1_packed = 0;
uint64_t winner2_packed = 0;

struct __attribute__((aligned(64))) ThreadStats {
    uint64_t iters;
};

struct ThreadStats thread_iters[NUM_THREADS];
uint64_t rep_iters[NUM_REPS] = {0};

void unpack_prefix(uint64_t packed, unsigned char* out_payload) {
    for (int i = prefix_len - 1; i >= 0; i--) {
        out_payload[i] = (char)(packed & 0xFF);
        packed >>= 8;
    }
    memcpy(out_payload + prefix_len, suffix, suffix_len);
    out_payload[prefix_len + suffix_len] = '\0';
}

void* worker(void *args){
    int thread_id = *(int*) args;

    unsigned int seed = (unsigned int)time(NULL) * (thread_id + 1) * (iter + 1) * 73856093;
    unsigned char to_bake[64]; 

    memcpy(to_bake + prefix_len, suffix, suffix_len);
    to_bake[prefix_len + suffix_len] = '\0';

    unsigned char candidate_hash[DIGEST_LENGTH];
    uint64_t iterations = 0;
    
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    while(!found_flag){
        
        uint64_t packed_prefix = 0;
        
        for(int i = 0; i < prefix_len; i++){
            unsigned char c = charset[rand_r(&seed) % 62];
            to_bake[i] = c;
            packed_prefix = (packed_prefix << 8) | c;
        }

        SHA256((unsigned char*) to_bake, prefix_len + suffix_len, candidate_hash);
        iterations++;
        
        uint64_t hash_val = 0;
        int bytes_to_match = NUM_BITS_TO_MATCH / 8;
        for(int j = 0; j < bytes_to_match; j++) {
            hash_val = (hash_val << 8) | candidate_hash[j];
        }

        uint64_t slot = (hash_val ^ (hash_val * 2654435761ULL)) & TABLE_MASK;
        
        uint128_t new_entry = ((uint128_t)hash_val << 64) | packed_prefix;
        uint128_t empty_entry = ~(uint128_t)0;

        while (1) {
            uint128_t old_entry = __sync_val_compare_and_swap(&hash_table[slot], empty_entry, new_entry);

            if (old_entry == empty_entry) {
                break;
            }
            else {
                uint64_t old_hash = (uint64_t)(old_entry >> 64);
                uint64_t old_id   = (uint64_t)old_entry;

                if (old_hash == hash_val) {
                    if (old_id != packed_prefix) {
                        if (__sync_bool_compare_and_swap(&found_flag, 0, 1)) {
                            winner1_packed = old_id;
                            winner2_packed = packed_prefix;
                        }
                    }
                    break;
                }
                else {
                    slot = (slot + 1) & TABLE_MASK;
                }
            }
        }
        
        if (thread_id == 0 && iterations % 250000 == 0) {
            printf("\rHashes checked: ~%llu <>", iterations * NUM_THREADS);
            fflush(stdout);
        }
    }

    thread_iters[thread_id].iters = iterations;
    return NULL;
}

void solve(int target){
    memset(hash_table, 0xFF, TABLE_SIZE * sizeof(uint128_t));
    pthread_t threads[NUM_THREADS];
    int threads_ids[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++){
        threads_ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &threads_ids[i]);
    }

    for(int i = 0; i < NUM_THREADS; i++){
        pthread_join(threads[i], NULL);
    }

    unsigned char p1[64], p2[64];
    unsigned char h1[32], h2[32];
    
    unpack_prefix(winner1_packed, p1);
    unpack_prefix(winner2_packed, p2);

    SHA256(p1, strlen((char*)p1), h1);
    SHA256(p2, strlen((char*)p2), h2);

    printf("Collision Found\n", iter + 1);
    printf("Payload 1: %s | Hash 1: ", p1);
    for(int l = 0; l < 32; l++) printf("%02x", h1[l]);

    printf("\nPayload 2: %s | Hash 2: ", p2);
    for(int l = 0; l < 32; l++) printf("%02x", h2[l]);
    printf("\n");

    uint64_t tot = 0; 
    for(int i = 0; i < NUM_THREADS; i++){
        tot += thread_iters[i].iters;
    }

    printf("Search Iteration %d complete. Total iterations: %llu \n\n", iter + 1, tot);
    rep_iters[iter] = tot;
    iter++;
    found_flag = 0;

    if(target > iter){
        solve(target);
    }
}

int main(){
    suffix_len = strlen(suffix);

    hash_table = (uint128_t*)malloc(TABLE_SIZE * sizeof(uint128_t));

    if (!hash_table) {
        printf("Out of Memory.\n");
        return 1;
    }

    solve(NUM_REPS);

    uint64_t sum = 0;
    printf("\n\n--- FINAL STATISTICS (%d REPS) ---\n", NUM_REPS);
    for(int i = 0; i < NUM_REPS; i++){
        sum += rep_iters[i];
        printf("%llu, ", rep_iters[i]);
    }
    
    double average = (double)sum / NUM_REPS;
    printf("\nAverage Iterations Taken: %f\n", average);
    
    free(hash_table);
    return 0;
}