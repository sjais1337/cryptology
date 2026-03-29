#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#include "sha256.cuh"

#define DIGEST_LENGTH 32
#define PREFIX_LEN 7


// The first few characters are blank space (basically first 3)
// since we have only 33 million threads here, thus the ids are 
// restricted to 33 million initially, but combining with the offset
// we eventually reach longer (non space-filled) payloads
__device__ void gen_str(uint64_t id, unsigned char* prefix){
    for(int i = PREFIX_LEN - 1; i >= 0; i--){
        prefix[i] = (char) ((id%94) + 33);
        id /= 94;
    }
}

// Kernel specifically for calculation of Target Hash
__global__ void gen_target(
    const unsigned char* data, 
    int len, 
    unsigned char* result
){
    SHA256_CTX ctx;
    sha256_init(&ctx);                  // initialize hashing state
    sha256_update(&ctx, data, len);     
    sha256_final(&ctx, result);
}


__global__ void main_kernel(
    unsigned char* target_hash,
    int num_bytes_to_match,
    unsigned char* suffix,
    int suffix_len,
    volatile int* found_flag, 
    unsigned char* found,
    uint64_t offset                     // offset = Multiple of threads per batch
) {
    uint64_t thread_id = offset + (uint64_t) blockIdx.x * blockDim.x + threadIdx.x;

    if (*found_flag == 1) return;

    unsigned char payload[64];
    unsigned char candidate_hash[DIGEST_LENGTH];

    gen_str(thread_id, payload);

    for(int i = 0; i < suffix_len; i++){ 
        payload[PREFIX_LEN + i] = suffix[i];
    }

    SHA256_CTX ctx; 
    sha256_init(&ctx);
    sha256_update(&ctx, payload, PREFIX_LEN + suffix_len);
    sha256_final(&ctx, candidate_hash);

    // to save extra computation
    bool match = true; 
    for(int i = 0; i< num_bytes_to_match; i++){
        if(candidate_hash[i] != target_hash[i]) {
            match = false;
            break;
        }
    }


    if (match) {
        if(atomicExch((int*) found_flag, 1) == 0) {
            for(int i = 0; i < PREFIX_LEN + suffix_len; i++){
                found[i] = payload[i]; 
            }
            found[PREFIX_LEN + suffix_len] = '\0';
        }
    }
}



int main() {
    const char *target = "shivanshj24@iitk.ac.in";
    int target_len = strlen(target);

    const char *suffix = "@iitk.ac.in";
    int suffix_len = strlen(suffix);

    int num_bits_to_match = 32; 
    int num_bytes_to_match = num_bits_to_match/8; 

    int h_found_flag = 0; 
    unsigned char h_found[64] = {0};
    // unsigned char h_target_hash[DIGEST_LENGTH] = {0};

    unsigned char   *d_target,
                    *d_target_hash, 
                    *d_suffix,
                    *d_found;
    
    int *d_found_flag;

    cudaMalloc((void**)&d_target, target_len);
    cudaMalloc((void**)&d_target_hash, DIGEST_LENGTH);
    cudaMalloc((void**)&d_suffix, suffix_len);
    cudaMalloc((void**)&d_found_flag, sizeof(int));
    cudaMalloc((void**)&d_found, 64);
       
    // Compute the target hash using specific kernel
    cudaMemcpy(d_target, target, target_len, cudaMemcpyHostToDevice);

    gen_target<<<1,1>>>(d_target, target_len, d_target_hash);
    cudaDeviceSynchronize();
    cudaFree(d_target);

    cudaMemcpy(d_suffix, suffix, suffix_len, cudaMemcpyHostToDevice);
    cudaMemcpy(d_found_flag, &h_found_flag, sizeof(int), cudaMemcpyHostToDevice);

    int threadPerBlock = 512; 
    int numBlocks = 65535;

    uint64_t threads_per_batch = (uint64_t) threadPerBlock * numBlocks; 
    uint64_t global_offset = 0;

    printf("Launching GPU. Target: %d. Number of Threads Launched: %llu", num_bits_to_match, threads_per_batch);

    // Now just keep launching the kernel till found_flag is 1. 

    while(!h_found_flag) {
        main_kernel<<<numBlocks, threadPerBlock>>>(
            d_target_hash,
            num_bytes_to_match,
            d_suffix, 
            suffix_len,
            d_found_flag,
            d_found, 
            global_offset
        );

        cudaDeviceSynchronize();
        cudaMemcpy(&h_found_flag, d_found_flag, sizeof(int), cudaMemcpyDeviceToHost);

        global_offset += threads_per_batch;
        printf("\rHashes Computed: %llu ", global_offset);
        fflush(stdout);
    }


    if(h_found_flag) {
        cudaMemcpy(h_found, d_found, 64, cudaMemcpyDeviceToHost);
        printf("\n\n Found Collision: %s", h_found);
    }

    cudaFree(d_target_hash);
    cudaFree(d_suffix);
    cudaFree(d_found_flag);
    cudaFree(d_found);
}