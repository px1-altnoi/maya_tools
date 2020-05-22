"""
clearer.py
LICENCE: MIT LICENCE
Author: Altnoi(px1)
version: 1.00
"""

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

select_items = pm.selected()

print("================Process Start==================\n")

for myNode in select_items:
    createCMD = myNode.getShape() + ".aiOpaque"
    myShape = myNode.getShape()
    
    mel.eval('string $myShape = "%s";' %myShape)
    
    if( mel.eval('attributeExists("aiOpaque", $myShape);')):
        cmds.setAttr(createCMD, 0)
    else:
        print("[INFO]" + myShape + " does not have aiAttribute\n")
    
print("================Process ENDED==================\n")
