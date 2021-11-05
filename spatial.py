import pymel.core as pm
import pymel.core.datatypes as dt

def aim_at_target(target, aim, aim_ax = 'x', up_ax ='y', up_vec = None, up_obj = None):
    #doc strings
    '''
    aim_at_target:
    This function will be used to adjust and correct the orientation of any node specified by the argument above

    '''
    #get into this habit of method checks
    if not (isinstance(target, pm.PyNode)):
        pm.error("Incorrect argument(s). Argument(s) must be PyNodes. ")
        return

    if not (target.type() in ['transform','joint']):
        pm.error("Argument(s) must be transform(s) or joint(s)")
        return
    
    #get positions of target and aim
    target_pos = dt.Vector(pm.xform(target, t=True, q=True, ws=True))
    aim_pos = dt.Vector(pm.xform(aim, t=True, q=True, ws=True))

    #identify vectors
    aim_vec = (aim_pos - target_pos)
    aim_vec.normalize()

    #This is here if I either
    # 1)DECIDE to keep the up vector at DEFAULT  
    # 2)Have an obj define my up_vec 
    # 3)Explicitly define the up vector in the arg of aim_at_target
    if (up_obj == None):
        if (up_vec == None):
            up_vec = dt.Vector(0,-1,0)
        else:
            up_vec = dt.Vector(up_vec)
    else:
        up_obj_pos = dt.Vector(pm.xform(up_obj, t=True, q=True, ws=True))
        up_vec = (target_pos - up_obj_pos)

    #finding the cross product
    cross_vec = aim_vec.cross(up_vec)
    cross_vec.normalize()
    up_vec = aim_vec.cross(cross_vec)
    up_vec.normalize()
    
    #input values into matrix
    m0= list(aim_vec)
    m1= list(up_vec)
    m2= list(cross_vec)
    m3= list(target_pos)
    
    #input values of constants (the fourth colomn of the matrix)
    m0.append(0.0)
    m1.append(0.0)
    m2.append(0.0)
    m3.append(1.0)
    
    #creating Matrix
    target_matrix = dt.Matrix(m0,m1,m2,m3)

    #orient and move "target" in viewport
    target.setMatrix(target_matrix, worldSpace=True)

