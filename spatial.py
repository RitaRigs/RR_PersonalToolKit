import pymel.core as pm
import pymel.core.datatypes as dt

def aim_at_target(target, aim):
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
    up_vec = dt.Vector(0,-1,0)

    #remind Retsyn to tell me that doing my own math is BAD. Have Maya do the work for you. Pointing Float Precision.
    #finding the cross product
    cross_vec = aim_vec.cross(up_vec)
    cross_vec.normalize()
    up_vec = aim_vec.cross(cross_vec)
    up_vec.normalize()
    
    #input values into matrix
    m0= list(aim_vec)
    m1= list(up_vec)
    m2= list(cross_vec)

    #constant values in matrix
    m3= [0,0,0,1.0]

    #input values into matrix
    m0.append(target_pos[0])
    m1.append(target_pos[1])
    m2.append(target_pos[2])
    
    #creating Matrix
    target_matrix = dt.Matrix(m0,m1,m2,m3)

    #orient and move "target" in viewport
    pm.xform(target, ws=True, m= target_matrix)

