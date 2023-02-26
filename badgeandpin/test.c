#include <stdio.h>
int main()
{
   char encoded_flag[] = {0xaf,
                          0x85,
                          0xde,
                          0xba,
                          0x7e,
                          0x78,
                          0x47,
                          0x5c,
                          0x97,
                          0xe2,
                          0xa0,
                          0xc5,
                          0x62,
                          0x1c,
                          0x3a,
                          0x30,
                          0x9c,
                          0xfe,
                          0xa3,
                          0xc5,
                          0x71,
                          0x67,
                          0x47,
                          0x36,
                          0x84,
                          0x9f,
                          0xde,
                          0xca,
                          0x1e,
                          0x79,
                          0x21,
                          0x34,
                          0x85,
                          0xe3,
                          0xc5,
                          0xe3};
   char decoded_flag[36];

   unsigned int guess_key = 
   for (unsigned int i = 0; i < 9; i++)
   {

      decoded_flag[i] = (unsigned int)encoded_flag[4 * i] ^ 0xaaaaaaaa;
   }
   

   return 0;
}