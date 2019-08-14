#ifndef __AES_NI_H__
#define __AES_NI_H__

#include <stdint.h>     //for int8_t
#include <string.h>     //for memcmp
#include <wmmintrin.h>  //for intrinsics for AES-NI
//compile using gcc and following arguments: -g;-O0;-Wall;-msse2;-msse;-march=native;-maes

//internal stuff

//macros
#define DO_ENC_BLOCK(m,k) 
    do
    {
        m = _mm_xor_si128       (m, k[ 0]); 
        m = _mm_aesenc_si128    (m, k[ 1]); 
        m = _mm_aesenc_si128    (m, k[ 2]); 
        m = _mm_aesenc_si128    (m, k[ 3]); 
        m = _mm_aesenc_si128    (m, k[ 4]); 
        m = _mm_aesenc_si128    (m, k[ 5]); 
        m = _mm_aesenc_si128    (m, k[ 6]); 
        m = _mm_aesenc_si128    (m, k[ 7]);
        m = _mm_aesenc_si128    (m, k[ 8]); 
        m = _mm_aesenc_si128    (m, k[ 9]); 
        m = _mm_aesenclast_si128(m, k[10]);
    }
    while(0)

#define DO_DEC_BLOCK(m,k) 
    do
    {
        m = _mm_xor_si128       (m, k[10+0]); 
        m = _mm_aesdec_si128    (m, k[10+1]); 
        m = _mm_aesdec_si128    (m, k[10+2]); 
        m = _mm_aesdec_si128    (m, k[10+3]); 
        m = _mm_aesdec_si128    (m, k[10+4]); 
        m = _mm_aesdec_si128    (m, k[10+5]); 
        m = _mm_aesdec_si128    (m, k[10+6]); 
        m = _mm_aesdec_si128    (m, k[10+7]); 
        m = _mm_aesdec_si128    (m, k[10+8]); 
        m = _mm_aesdec_si128    (m, k[10+9]); 
        m = _mm_aesdeclast_si128(m, k[0]);\
    }
    while(0)
        

printf("hello")