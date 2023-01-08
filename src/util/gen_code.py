
tot_mem_list = [200 * 1024, 300 * 1024, 400 * 1024, 500 * 1024, 600 * 1024, 700 * 1024, 800 * 1024,
                    900 * 1024, 1000 * 1024, 1100 * 1024]
heavy_mem_list = [100 * 1024, 100 * 1024, 100 * 1024, 100 * 1024, 100 * 1024, 150 * 1024, 150 * 1024,
                      150 * 1024, 150 * 1024, 200 * 1024]
# heavy_mem_list = [min(max(8 0 *1024 , i * 3/ /10) ,20 0 *1024) for i in tot_mem_list]
for i in range(8):


    # print('DivSketch<{0} / COUNTER_PER_BUCKET / 8, {1}> *div{2} = new DivSketch<({0} / COUNTER_PER_BUCKET /8), {1}>();'.format(heavy_mem_list[i],tot_mem_list[i],i+1))
    # print("int dist{0} = std::abs(it->second - est_val{0});".format(i+1))
    # print("ARE[{0}] += dist{0} * 1.0 / (it->second);".format(i+1))
    # print("absE[{0}] += dist{0} * 1.0;".format(i+1))
    # print("measure[{0}] += est_val{0};".format(i+1))
    # print("measure[{0}] += est_val{0};".format(i+1))
    # print("measure[{0}] += est_val{0};".format(i+1))
    # print("precesion[{0}] = TP[{0}] / (double) heavy_hitters{0}.size();".format(i+1))
    # print("vector< pair<string, int> > heavy_hitters{0};\ndiv{0}->get_heavy_hitters(HEAVY_HITTER_THRESHOLD(packet_cnt), heavy_hitters{0});".format(i+1))
    # print("for(int k = 0; k < (int)heavy_hitters{0}.size(); ++k){{\nstring key = heavy_hitters{0}[k].first;\nif("
    #       "Real_heavy_hitters.find(key) "
    #       "!=Real_heavy_hitters.end())\n{{\nTP[{0}] += 1;\n}}}}".format( i +1))
    # print("WMRE_up[{0}] += dist{0};".format(i+1))
    # print("WMRE_down[{0}] +=  (est_val{0}+it->second)/2.0;".format(i+1))
    # print("int real_fm{0}[500000]={{0}};".format(i+1))
    # print("est_fm{0}[est_val{0}]++;".format(i+1))
    # print("WMRE_up[{0}] += abs(est_fm{0}[j] - real_fm[j]);\nWMRE_down[{0}] += abs(est_fm{0}[j] + real_fm[j]);".format(i+1))
    # print("unordered_map<int, int> est_fm{0};".format(i+1))
    # print("est_ce[{0}] = div{0}->get_cardinality();".format(i+1))
    # print("Register<bit<32>, bit<32>>(1600,0) hash_tbl_count{0};".format(i+1))
    # print("Register<bit<32>, bit<32>>(1600,0) hash_tbl_value{0};".format(i+1))
    pass
#bf-sde.pipe_mgr.stful-mgr>
# for i in range(2,9):
#     print("""
#     RegisterAction<HASH_TABLE_KEY_BIT_WIDTH_t, bit<32>, HASH_TABLE_KEY_BIT_WIDTH_t>(hash_tbl_key{0})
#     check_key{0} = {{
#         void apply(inout HASH_TABLE_KEY_BIT_WIDTH_t register_data, out CHECK_FLAG result) {{
#             if(register_data != 0){{
#                 if(register_data == meta.flow_id){{
#                     result = 1;
#                 }}else{{
#                     result = 0;
#                 }}
#             }}else{{
#                 result = 1;
#                 register_data = meta.flow_id;
#             }}
#             // register_data = register_data |+| 1;
#         }}
#     }};
#
#     RegisterAction<HASH_TABLE_COUNT_BIT_WIDTH_t, bit<32>, HASH_TABLE_COUNT_BIT_WIDTH_t>(hash_tbl_count{0})
#     count_packet{0} = {{
#         void apply(inout HASH_TABLE_COUNT_BIT_WIDTH_t register_data) {{
#             register_data = register_data |+| 1;
#         }}
#     }};
#     """.format(i))


for i in range(2,9):
    print("""
    else if(check_key{0}.execute(meta.index_sketch1)==1){{
            count_packet{0}.execute(meta.index_sketch1);
        }}""".format(i))

