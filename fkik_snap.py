import pymel.core as pm
import pymel.core.datatypes as dt

'''
Rita Rigs
11-4-2021

'''

def pv_build(base_jnt, mid_jnt, end_jnt, mag =0.1):
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
        


    #def create_ik( side):
        #leg_ik = pm.ikHandle(sj=IK_jnt_list[0] , ee=IK_jnt_list[2] , n=(side+"_Leg_IK"))[0]
        #leg_pv = pm.poleVectorConstraint(pv_ctrl, leg_ik)

