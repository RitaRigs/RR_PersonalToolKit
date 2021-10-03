import pymel.core as pm

def single_batch_connect(out_attr, in_attr):
    ''' 
    Connects one output of one node to multiple inputs

    usage:
    (using maya selection)
    single_batch_connect(out_attr, in_attr)
    out_attr/ string
    in_attr/ string
    '''
    sel = pm.ls(sl=True)
    source = sel[0]
    target = sel[1:]

    for node in target:
        pm.connectAttr(source.name()+'.'+ out_attr, node.name()+'.'+in_attr)
        print("Connecting {} to {}".format(source.name()+'.'+out_attr, node.name()+'.'+in_attr))


def multi_batch_connect(out_attr, in_attr):
    '''
    Connects multiple outputs to multiple inputs in a one-to-one fashion

    Select nodes in pairs of SOURCE then TARGET

    usage:
    (using maya selection)
    multi_batch_connect(out_attr, in_attr)
    out_attr/string
    in_attr/ string
    '''
    sel = pm.ls(sl=True)
    if((len(sel) % 2) != 0):
        pm.error("Must be an even number of selected nodes!")
        return
    
    sources = []
    targets = []

    for val in sel:
        if ((sel.index(val) % 2) ==0):
            sources.append(val)
        else:
            targets.append(val)

    zip_list = zip(sources, targets)
    for pair in zip_list:
        pm.connectAttr(pair[0].name()+'.'+out_attr, pair[1].name()+'.'+in_attr)


