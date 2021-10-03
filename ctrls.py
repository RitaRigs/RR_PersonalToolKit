import pymel.core as pm
import pymel.core.datatypes as dt


def create_ctrls(target = None , name="", color=4, side="", orient=True, sub=False, hierarchy=[]):
    if(target == None):
        sel = pm.ls(sl=True)[0]
    else:
        sel = target
    new_trans = pm.createNode('transform', n=(name + "_NULL"))
    if(orient):
        pm.matchTransform(new_trans, sel, pos= True, rot = True)
    else:
        pm.matchTransform(new_trans, sel, pos= True, rot= False)

#gather information on the curves to store them as a custom controller shape.
def learn_curve():
    #create the custom shape first and then select it. Turn selection into a PyNode
    #plug the curve into the "curve info" to gather the proper information
    #print info to create library for that controller shape
    target_curve= pm.ls(sl=True)[0]
    curv_info = pm.createNode('curveInfo')
    curv_shape= target_curve.getShape()
    print(target_curve.type())

    curv_shape.worldSpace >> curv_info.inputCurve 

    pt_vecs=[]

    for cv in curv_shape.cv:
        print(cv)
        new_pt_vec = pm.getAttr(cv)
        pt_vecs.append(new_pt_vec.get())

    print(pt_vecs)
    knots = curv_info.knots.get()
    degree = curv_shape.degree()

    curv_dict = {}
    curv_dict['knots'] = knots
    curv_dict['degrees'] = degree
    curv_dict['points'] = pt_vecs

    print(curv_dict)

    return curv_dict

