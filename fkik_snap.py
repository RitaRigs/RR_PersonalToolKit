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
        
def fk_to_ik(side, limb, fk_ctrls= None, ik_jnts= None):
    
    #specify the limb
    if(limb=='leg'):
        target_list=["hip", "knee", "ankle"]
    elif(limb=='arm'):
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
    
    if(side != None):
        if(side.upper() in ['L','LEFT','L_','_L', 'LFT','LT']):
            side_token=const.side_dict['left']
        elif(side.upper() in ['R','R_','_R','RIGHT','RGT','RT']):
            side_token=const.side_dict['right']
        elif(side.upper() in ['C','C_','_C','CENTER','CENTRE','CNT','CT']):
            side_token=const.side_dict['centre']
    else:
        pm.error("No side specified.")
    
        
        


def ik_to_fk():
    pass