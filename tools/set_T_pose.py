import glob

for f in glob.glob("/home/kia/MOTION_ESTIMATION/bandai-namco/*"):
    print(f)
    new_f_name = "T_pose_"+f.split("/")[-1]
    frame_time_check = False

    with open(f, "r+") as f_read:

        with open(f"/home/kia/MOTION_ESTIMATION/bandai-namco_T_pose/{new_f_name}", "w+") as f_write:

            for line in f_read:

                if "Frames" in line:
                    line_cleaned = line.replace(" \n","") if " \n" in line else line.replace("\n","")
                    frame_number = int(line_cleaned.split(" ")[-1]) + 1
                    new_frame_line = f"Frames: {frame_number} \n"
                    f_write.write(new_frame_line)
                    continue
                
                if frame_time_check:
                    line_cleaned = line.replace(" \n","") if " \n" in line else line.replace("\n","")
                    motion_values = line_cleaned.split(" ")
                    n_motions = len(motion_values)
                    new_motion_line = f"{motion_values[0]} {motion_values[1]} {motion_values[2]}" + " 0"*(n_motions - 3) + " \n"
                    frame_time_check = False
                    f_write.write(new_motion_line)
                
                if "Frame Time" in line:
                    frame_time_check = True

                f_write.write(line)
