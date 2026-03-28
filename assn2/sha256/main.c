#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <openssl/sha.h>

#define DIGEST_LENGTH 32

void main(){
    const char *data = "shivanshj24@iitk.ac.in";
    unsigned char target_hash[DIGEST_LENGTH];

    SHA256((unsigned char*) data, strlen(data), target_hash);

    const char *suffix = "@iitk.ac.in";
    size_t suffix_len = strlen(suffix);

    // If we wish to compare the first 24 bits, then we should ideally be 
    // looping through more numbers.
    size_t num_bits_to_match = 24;
    size_t num_bytes_to_match = num_bits_to_match/8;

    size_t num_bits_to_loop = num_bits_to_match + 8;
    size_t num_bytes_to_loop = num_bits_to_loop/8;

    unsigned char *to_bake = (unsigned char *) malloc(num_bytes_to_loop + suffix_len + 1);
    memcpy(to_bake + num_bytes_to_loop, suffix, suffix_len);
    to_bake[num_bytes_to_loop + suffix_len] = '\0';

    unsigned char candidate_hash[DIGEST_LENGTH];

    for(uint64_t i = 0; i < (1LL << num_bits_to_loop); i++){

        uint64_t temp = i;
        for (int b = num_bytes_to_loop - 1; b >= 0; b--) {
            to_bake[b] = (unsigned char)((temp % 95) + 32);
            temp /= 95;
        }

        SHA256((unsigned char*) to_bake, num_bytes_to_loop + suffix_len, candidate_hash);

        if(memcmp(candidate_hash, target_hash, num_bytes_to_match) == 0) {
            printf("Found a collision in first %d bits!\n\nTarget Hash: ", num_bits_to_match);

            for(int l = 0; l < DIGEST_LENGTH; l++){
                printf("%02x", *(target_hash + l));
            }

            printf("\nColliding Hash: ");
            for(int l = 0; l < DIGEST_LENGTH; l++){
                printf("%02x", *(candidate_hash + l));
            }

            printf("\n\n");

            printf("Number of iterations taken: %d\n", i);
            printf("Colliding Payload: %s\n", to_bake);

            break;
        }
    }

    free(to_bake);
}