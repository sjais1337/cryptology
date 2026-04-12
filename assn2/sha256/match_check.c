#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <openssl/sha.h>
#include <time.h>
#include <pthread.h>

#define DIGEST_LENGTH 32

#define NUM_THREADS 16
#define NUM_REPS 50
#define NUM_BITS_TO_MATCH 24

unsigned char target_hash[DIGEST_LENGTH];
size_t num_bytes_to_match;

const char *suffix = "@iitk.ac.in";
size_t suffix_len;

int iter = 0;
volatile int found_flag = 0;
const int prefix_len = 7;

uint64_t thread_iters[NUM_THREADS] = {0};
uint64_t rep_iters[NUM_REPS] = {0};

void* worker(void *args){
    int thread_id = *(int*) args;

    unsigned int seed = time(NULL) ^ (thread_id * 1999) ^ (iter * 6666);
    unsigned char *to_bake = (unsigned char *) malloc(prefix_len + suffix_len + 1);

    memcpy(to_bake + prefix_len, suffix, suffix_len);
    to_bake[prefix_len + suffix_len] = '\0';

    unsigned char candidate_hash[DIGEST_LENGTH];
    uint64_t iterations = 0;

    while(!found_flag){

        for(int i = 0; i < prefix_len; i++){
            to_bake[i] = (char) ((rand_r(&seed) % 95) + 32);
        }

        SHA256((unsigned char*) to_bake, prefix_len + suffix_len, candidate_hash);
        iterations++;
        
        if(memcmp(candidate_hash, target_hash, num_bytes_to_match) == 0) {
            if(!found_flag) {
                found_flag = 1;
                printf("Collision Found\n");
                printf("Payload 1: shivanshj@iitk.ac.in | Hash 1: ");

                for(int l = 0; l < DIGEST_LENGTH; l++){
                    printf("%02x", *(target_hash + l));
                }

                printf("\nPayload 2: %s | Hash 2: ", to_bake);
                for(int l = 0; l < DIGEST_LENGTH; l++){
                    printf("%02x", *(candidate_hash + l));
                }

                printf("\n");
                break;
            }
        }


        if (thread_id == 0 && iterations % 250000 == 0) {
            printf("\rHashes checked: ~%llu <> ", iterations * NUM_THREADS);
            fflush(stdout);
        }
    }

    thread_iters[thread_id] = iterations;



    free(to_bake); 
    return NULL;
}

void solve(int target){
    pthread_t threads[NUM_THREADS];
    int threads_ids[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++){
        threads_ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &threads_ids[i]);
    }

    for(int i = 0; i < NUM_THREADS; i++){
        pthread_join(threads[i], NULL);
    }

    uint64_t tot = 0; 
    for(int i = 0; i < NUM_THREADS; i++){
        tot += thread_iters[i];
    }

    printf("Search Iteration %d complete. Total iterations: %lld \n\n", iter, tot);
    rep_iters[iter] = tot;
    iter++;
    found_flag = 0;

    if(target > iter){
        solve(target);
    }
}


int main(){
    const char *data = "shivanshj24@iitk.ac.in";
    SHA256((unsigned char*) data, strlen(data), target_hash);
    suffix_len = strlen(suffix);

    num_bytes_to_match = NUM_BITS_TO_MATCH/8;

    solve(NUM_REPS);

    uint64_t sum = 0;
    printf("\n\n--- FINAL STATISTICS (%d REPS) ---\n", NUM_REPS);
    for(int i = 0; i < NUM_REPS; i++){
        sum += rep_iters[i];
        printf("%d, ", rep_iters[i]);
    }

    double average = (double) sum/NUM_REPS;
    printf("\nAverage Iterations Taken: %f\n", average);

    return 0;
}

