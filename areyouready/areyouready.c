#include <stdio.h>
int main() {
   char text[] = "@r3_y0u_r3@dy?_g3t_up,_g3t_up_g3t_up,_g3t_up_g3t_up,_g3t_up__g3t_up,_g3t_up_g3t_up,_g3t_up_g3t_up,_g3t_up__w3ll,_@r3_y0u_r3@dy_n0w?_f0r_th3_r3v0luti0n_f0r_t00_l0ng_y0ur_p0w3r_h@s_b33n_t@k3n_@w@y_it's_b33n_t@k3n_@w@y_d03s_y0ur_h3@rt_f33l_h3@vy_n0w_s@v0r_th3_s0luti0n_t@k3_th0s3_m3nt@l_sh@ckl3s_0ff_@nd_thr0w_th3m_@w@y_y0u'v3_g0t_t0_g3t_th3m_0ut_0f_y0ur_mind_d0n't_y0u_l3t_th3ir_visi0n_l3@v3_y0u_blind__m0ving_st3@dy_n0w_it's_@_r3v3l@ti0n_f0r_s0_l0ng_y0ur_f0cus_h@s_b33n_t@k3n_@w@y_n0w_y0u'r3_br3@king_@w@y_th3y_think_th3y_kn0w_y0u_but_h3r3's_@n_3duc@ti0n_n0_th3y_c@n't_c0ntr0l_y0u_0nc3_y0u'v3_br0k3n_@w@y_th3y'r3_d0n3_p@tr0lling_y0ur_mind_wh3n_th3y'r3_s3@rching_f0r_y0u,_th3y_will_find_@_f0rc3_th3y_@r3n't_r3@dy_f0r__@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_str0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_pr0v3_th3m_wr0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_turn3d_int0_s0m30n3_wh0_c@nn0t_b3_pr3y3d_up0n__th@t's_3n0ugh_@lr3@dy_n0w_y0u_d0n't_w@nt_t0_t@k3_it_@ll_y0ur_r3s3rv@ti0ns_h@v3_b33n_t@k3n_@w@y_th3y'v3_b33n_t@k3n_@w@y_s0_y0u_think_y0u'r3_r3@dy_n0w_f0r_th3_r3v0luti0n_y3@h,_th3y_c@n't_c0ntr0l_y0u_0nc3_y0u'v3_br0k3n_@w@y_y0u'v3_g0t_t0_g3t_th3m_0ut_0f_y0ur_mind_wh3n_th3y_st@nd_b3f0r3_y0u_th3y_will_find_@_f0rc3_th3y_@r3n't_r3@dy_f0r__@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_str0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_pr0v3_th3m_wr0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_turn3d_int0_s0m30n3_wh0_c@nn0t_b3_pr3y3d_up0n__@r3_y0u_r3@dy?__y0u_g0t_t0_g3t_th3m_0ut_0f_y0ur_mind_wh3n_th3y_st@nd_b3f0r3_y0u_th3y_will_find_@_f0rc3_th3y_@r3n't_r3@dy_f0r__@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_str0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_pr0v3_th3m_wr0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_y0u_t0_b3_turn3d_int0_s0m30n3_wh0_c@nn0t_b3_pr3y3d_up0n__@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_us_t0_b3_str0ng_@r3_y0u_r3@dy?_th3y_@r3n't_r3@dy_f0r_us_t0_pr0v3_th3m_wr0ng_@r3_y0u_r3@dy?_l3t_m3_kn0w_y0u'r3_r3@dy_f0r_y0u_t0_b3_turn3d_int0_p30pl3_wh0_c@nn0t_b3_pr3y3d_up0n__@r3_y0u_r3@dy?_@r3_y0u_r3@dy?_@r3_y0u_r3@dy?_y0u_c@nn0t_b3_pr3y3d_up0n_@r3_y0u_r3@dy?_@r3_y0u_r3@dy?_@r3_y0u_r3@dy?";
   int offset = 0x37a;
   unsigned int print_len = 0x21;
   char flag_open[] = "flag{";
   char flag_close[] = "}";
   printf("%s%.*s%s\n",flag_open, print_len, text + offset, flag_close);
   return 0;
}