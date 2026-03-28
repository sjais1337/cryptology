#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <openssl/sha.h>
#include <time.h>
#include <pthread.h>

#define DIGEST_LENGTH 32
#define NUM_THREADS 16

unsigned char target_hash[DIGEST_LENGTH];
size_t num_bytes_to_match;

const char *suffix = "@iitk.ac.in";
size_t suffix_len;

volatile int found_flag = 0;

const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
const size_t charset_size = 62;
const int prefix_len = 6;

uint64_t thread_iters[NUM_THREADS] = {0};

void* worker(void *args){
    int thread_id = *(int*) args;

    unsigned int seed = time(NULL) ^ (thread_id * 1999);
    unsigned char *to_bake = (unsigned char *) malloc(prefix_len + suffix_len + 1);

    memcpy(to_bake + prefix_len, suffix, suffix_len);
    to_bake[prefix_len + suffix_len] = '\0';

    unsigned char candidate_hash[DIGEST_LENGTH];
    uint64_t iterations = 0;

    while(!found_flag){
        for(int i = 0; i < prefix_len; i++){
            to_bake[i] = charset[rand_r(&seed) % charset_size];
        }

        SHA256((unsigned char*) to_bake, prefix_len + suffix_len, candidate_hash);
        iterations++;
        
        if(memcmp(candidate_hash, target_hash, num_bytes_to_match) == 0) {
            if(!found_flag) {
                found_flag = 1;
                printf("Found a collision!\n\nTarget Hash: ");

                for(int l = 0; l < DIGEST_LENGTH; l++){
                    printf("%02x", *(target_hash + l));
                }

                printf("\nColliding Hash: ");
                for(int l = 0; l < DIGEST_LENGTH; l++){
                    printf("%02x", *(candidate_hash + l));
                }

                printf("\n\n");

                printf("Colliding Payload: %s\n", to_bake);

                break;
            }
        }
    }

    thread_iters[thread_id] = iterations;

    free(to_bake); 
    return NULL;
}


int main(){
    const char *data = "shivanshj24@iitk.ac.in";
    SHA256((unsigned char*) data, strlen(data), target_hash);

    suffix_len = strlen(suffix);

    // If we wish to compare the first 24 bits, then we should ideally be 
    // looping through more numbers.
    size_t num_bits_to_match = 24;
    num_bytes_to_match = num_bits_to_match/8;

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

    printf("Search complete. Total iterations: %lld \n", tot);
    return 0;
}