import pymel.core as pm
import pymel.core.datatypes as dt
import constants as const

'''
Rita Rigs
11-4-2021

'''

def pv_build(base_jnt, mid_jnt, end_jnt, mag = 0.1):
        base_jnt = pm.PyNode(base_jnt)
        mid_jnt = pm.PyNode(mid_jnt)
        end_jnt = pm.PyNode(end_jnt)
        base_vec= dt.Vector(base_jnt.getTranslation(space='world'))
        end_vec= dt.Vector(end_jnt.getTranslation(space='world'))
        mid_vec= dt.Vector(mid_jnt.getTranslation(space='world'))
        base_mid_vec= base_vec-mid_vec
        base_mid_vec.normalize()
        mid_end_vec= end_vec - mid_vec
        mid_end_vec.normalize()
        pv = (base_mid_vec + mid_end_vec) * mag
        pv_pos = mid_vec - pv
        pv_loc = pm.spaceLocator(n=("PV_Loc"))
        pv_loc.translate.set(pv_pos)
        pv_loc.scaleX.set(0.05)
        pv_loc.scaleY.set(pv_loc.scaleX.get())
        pv_loc.scaleZ.set(pv_loc.scaleX.get())
        
def fk_to_ik(side, limb, ctrl_tag = None, jnt_tag = None, fk_ctrls= None, ik_jnts= None, order="s_n_t"):
    
    #specify the limb
    if(limb.upper() =='LEG'):
        target_list=["hip", "knee","ankle"]
    elif(limb.upper() =='ARM'):
        target_list=["shoulder","elbow","wrist"]
    else:
        pm.warning("Is it an arm or a leg?")
        return

    # Assign defaults to dodge mutable default arguments
    if(ik_jnts is None):
        local_ik_jnts_dict = const.ik_limbs_dict.copy()
    else:
        local_ik_jnts_dict = ik_jnts.copy()

    if(fk_ctrls is None):
        local_fk_ctrls_dict = const.fk_limbs_dict.copy()
    else:
        local_fk_ctrls_dict = fk_ctrls.copy()

    #specify the suffix/type
    if(ctrl_tag is None):
        ctrl_tag=const.suffix_dict['control']
    if(jnt_tag is None):
        jnt_tag=const.suffix_dict['joint']
    
    if(side is not None):
        if(side.upper() in ['L','LEFT','L_','_L', 'LFT','LT']):
            side_token=const.side_dict['Left']
        elif(side.upper() in ['R','R_','_R','RIGHT','RGT','RT']):
            side_token=const.side_dict['Right']
        elif(side.upper() in ['C','C_','_C','CENTER','CENTRE','CNT','CT']):
            side_token=const.side_dict['Centre']
    else:
        pm.error("No side specified.")
    
    ik_part_list=[]
    fk_part_list=[]
    for part in target_list:
        ik_node_string = ''
        fk_node_string = ''
        for char in order:
            if(char == 's'):
                ik_node_string += side_token
                fk_node_string += side_token
            elif(char == 'n'):
                ik_node_string += local_ik_jnts_dict[part]
                fk_node_string += local_fk_ctrls_dict[part]
            elif(char == 't'):
                ik_node_string += jnt_tag
                fk_node_string += ctrl_tag
            elif(char == '_'):
                if(len(ik_node_string)> 0):
                    if(ik_node_string[-1]!='_'):
                        ik_node_string += '_'
                if(len(fk_node_string)> 0):
                    if(fk_node_string[-1]!='_'):
                        fk_node_string += '_'
            else:
                pm.error("Invalid character in order arg. Must be 's','n','t', or '_' . ")
        ik_part_list.append(ik_node_string)
        fk_part_list.append(fk_node_string)
    print(ik_part_list)
    print(fk_part_list)

def ik_to_fk():
    pass