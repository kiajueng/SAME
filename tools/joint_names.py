import glob


unique_joints = []
for i,f in enumerate(glob.glob("/home/kia/MOTION_ESTIMATION/bandai-namco_T_pose_rename_joints/*")):
    print(f)
    with open(f,"r+") as f_read:
        for line in f_read:
            do_append = True
            if (("ROOT" in line) or ("JOINT" in line)):
                line_cleaned = line.strip()
                joint = line_cleaned.split(" ")[1]

                for j in unique_joints:
                    if j == joint:
                        do_append = False
                        
                if do_append:
                    unique_joints.append(joint)
                    do_append=True

with open("/home/kia/MOTION_ESTIMATION/SAME/tools/unique_joints.txt","w+") as f_write:
    for joint in unique_joints:
        f_write.write(joint + " \n")
