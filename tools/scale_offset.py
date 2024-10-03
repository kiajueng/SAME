import glob

for i,f in enumerate(glob.glob("/home/kia/MOTION_ESTIMATION/DATA_BANDAI_NAMCO/bandai-namco_T_pose_rename_joints/*")):
    print(f)
    new_fname = f.split("/")[-1]
    with open(f,"r+") as f_read:
        with open(f"/home/kia/MOTION_ESTIMATION/DATA_BANDAI_NAMCO/bandai-namco_T_pose_rename_joints_scaled_offsets/scaled_{new_fname}","w+") as f_write:
            for line in f_read:
                if ("OFFSET" in line):
                    tabs = line.split("OFFSET")[0]
                    line_cleaned = line.strip()
                    offsets = line_cleaned.split(" ")
                    offsets_float_scaled = [float(offset)*100 for i,offset in enumerate(offsets) if i > 0 ]                
                    new_line_scaled = f"{tabs}OFFSET {offsets_float_scaled[0]} {offsets_float_scaled[1]} {offsets_float_scaled[2]} \n" 
                    f_write.write(new_line_scaled)
                else:
                    f_write.write(line)
