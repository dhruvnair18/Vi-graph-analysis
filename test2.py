# import os
# #step 4c
# #deleting all files in the folder ChangedFiles


# def delete_files_in_directory(folder_path):
#     try:
#      files = os.listdir(folder_path)
#      for file in files:
#        file_path = os.path.join(folder_path, file)
#        if os.path.isfile(file_path):
#          print(os.remove(file_path))
#          os.remove(file_path)
#      print("All files from CIR/ChangedFiles deleted successfully.")
#     except OSError:
#      print("Error occurred while deleting files.")

# folder_path="C:/Users/naird/OneDrive - Dun and Bradstreet/Documents/Productions/New CDP Folder Structure/CIR/ChangedFiles"
# delete_files_in_directory(folder_path)
# import os
# import shutil

# src = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/RAW Unity Files"
# trg1 = r"Z:\Dhruv(Intern)\Productions\New CDP Folder Structure\MasterFile"
# heatmap= r"Z:\Dhruv(Intern)\Communal Stuff\New MasterFile Reports\csv"
# def copy_files_from_reports(src_dir, trg1_dir):
#     try:
#         for root, dirs, files in os.walk(src_dir):
#             if os.path.basename(root) == "MasterFile":
#                 for fname in files:
#                     src_file_path = os.path.join(root, fname)
#                     trg1_file_path = os.path.join(trg1_dir, fname)

#                     print("\nCopying file:", src_file_path)
#                     shutil.copy2(src_file_path, trg1_file_path)
        
#         print("\nAll files from RAW Unity Files' Reports folders copied to MasterFile.")
    
#     except Exception as e:
#         print("An error occurred:", str(e))

# copy_files_from_reports(src, trg1)
# try:
#     for item in os.listdir(trg1):
#         if os.path.isfile(os.path.join(trg1, item)):
#             if item.startswith('2024'):
#                   shutil.copy2(os.path.join(trg1, item), heatmap)
#                   print(f"\n Copied {item} to {heatmap}")
#     print("\n File from MasterFile copied successfully to Heatmap folder.")
# except OSError:
#     print("\n Error occurred while copying File from MasterFile copied successfully to Heatmap folder.")
    

# # source_folder="C:/Users/naird/OneDrive - Dun and Bradstreet/Documents/Productions/New CDP Folder Structure/CIR/ChangedFiles"

# # for item in os.listdir(trg1):
# #     if os.path.isfile(os.path.join(trg1,item)):
# #         if item.startswith('202'):
# #             try:
# #                 os.rename(os.path.join(trg1,item), os.path.join(trg1,"MasterFileMDA"))
# #                 print(f"File {item} renamed to MasterFileMDA")
# #             except PermissionError:
# #                 continue
# #             except Exception as e:
# #                     raise Exception(e)


# # import os

# # source_folder = "C:/Users/naird/OneDrive - Dun and Bradstreet/Documents/Productions/New CDP Folder Structure/CIR/ChangedFiles"

# try:
#     # Check if the old file named MasterFileMDA exists and delete it
#     old_file_path = os.path.join(trg1, "MasterFileMDA")
#     if os.path.isfile(old_file_path):
#         os.remove(old_file_path)
#         print(f"Old file MasterFileMDA deleted from {trg1}")
#     else:
#         print("No old file named MasterFileMDA found to delete.")

#     # Iterate through the files in the source folder
#     for item in os.listdir(trg1):
#         if os.path.isfile(os.path.join(trg1, item)):
#             if item.startswith('202'):
#                 try:
#                     new_file_path = os.path.join(trg1, "MasterFileMDA")
#                     os.rename(os.path.join(trg1, item), new_file_path)
#                     print(f"File {item} renamed to MasterFileMDA")
#                 except PermissionError:
#                     print(f"Permission denied when trying to rename {item}.")
#                     continue
#                 except Exception as e:
#                     print(f"Error occurred while renaming {item}: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# import os
# import shutil

# source = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/RAW Unity Files"
# target = r"Z:\Dhruv(Intern)\Productions\New CDP Folder Structure\CIS\ChangedFiles"
# pdf_folder = r"Z:\Dhruv(Intern)\Productions\New CDP Folder Structure\CIS\PDF"
# html_folder = r"Z:\Dhruv(Intern)\Productions\New CDP Folder Structure\CIS\HTML"

# def copy_and_rename_files(src_dir, trg1_dir):
#     try:
#         # Walk through all subdirectories in src_dir
#         for root, dirs, files in os.walk(src_dir):
#             if os.path.basename(root) == "CIS":
#                 # Look for HTML and PDF folders within CIS
#                 for subdir in ["HTML", "PDF"]:
#                     subfolder_path = os.path.join(root, subdir)
#                     if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
#                         for fname in os.listdir(subfolder_path):
#                             src_file_path = os.path.join(subfolder_path, fname)
#                             trg1_file_path = os.path.join(trg1_dir, fname)

#                             print("\nCopying file:", src_file_path)
#                             shutil.copy2(src_file_path, trg1_file_path)

#         print("\nAll files from CIS/HTML and CIS/PDF folders copied to CIS/ChangedFiles.")

#         # Check and rename files in the target directory
#         for fname in os.listdir(trg1_dir):
#             file_path = os.path.join(trg1_dir, fname)

#             if os.path.isfile(file_path):
#                 if "China Mainland" in fname:
#                     new_file_path_1 = os.path.join(trg1_dir, fname.replace("China Mainland", "China"))
#                     new_file_path_2 = os.path.join(trg1_dir, fname.replace("China Mainland", "Mainland China"))

#                     shutil.copy2(file_path, new_file_path_1)
#                     os.rename(file_path, new_file_path_2)
#                     print(f"Renamed {fname} to Mainland China and created a copy as China in {trg1_dir}")

#                 elif "Spain" in fname:
#                     new_file_path = os.path.join(trg1_dir, fname.replace("Spain", "Bhandup"))

#                     shutil.copy2(file_path, new_file_path)
#                     print(f"Created a copy of {fname} as Turkey in {trg1_dir}")

#     except Exception as e:
#         print("An error occurred:", str(e))

# # Call the function to copy and rename files
# copy_and_rename_files(source, target)

import os
#step 4c
#deleting all files in the folder ChangedFiles
print("step 4c \n")
def delete_files_in_directory(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                print("Deleting file:", file_path)
                os.remove(file_path)
        print("All files from CIR/ChangedFiles deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")

folder_path = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/CIR/ChangedFiles"
delete_files_in_directory(folder_path)

#copying and pasting all files from RAW Unity Files

# folder_path2="C:/Users/naird/OneDrive - Dun and Bradstreet/Documents/Productions/New CDP Folder Structure/RAW Unity Files/Reports"

#from pathlib import Path
import shutil

src = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/RAW Unity Files"
trg1 = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/CIR/ChangedFiles"
trg2 = "Z:/Dhruv(Intern)/Productions/New CDP Folder Structure/CIR/PDF"

def copy_and_rename_files(src_dir, trg1_dir, trg2_dir):
    try:
        # Copy files from source to target directories
        for root, dirs, files in os.walk(src_dir):
            if os.path.basename(root) == "CIR":
                for fname in files:
                    src_file_path = os.path.join(root, fname)
                    trg1_file_path = os.path.join(trg1_dir, fname)
                    trg2_file_path = os.path.join(trg2_dir, fname)
                    
                    print("\nCopying file:", src_file_path)
                    shutil.copy2(src_file_path, trg1_file_path)
                    shutil.copy2(src_file_path, trg2_file_path)
                    
        print("\nAll files from 'RAW Unity Files' CIR folders copied to CIR/ChangedFiles and CIR/PDF.")
        
        # Check and rename files in target directories
        for target_dir in [trg1_dir, trg2_dir]:
            for fname in os.listdir(target_dir):
                file_path = os.path.join(target_dir, fname)
                
                if os.path.isfile(file_path):
                    if "China Mainland" in fname:
                        new_file_path_1 = os.path.join(target_dir, fname.replace("China Mainland", "China"))
                        new_file_path_2 = os.path.join(target_dir, fname.replace("China Mainland", "Mainland China"))
                        
                        shutil.copy2(file_path, new_file_path_1)
                        os.rename(file_path, new_file_path_2)
                        
                        print(f"Renamed {fname} to Mainland China and created a copy as China in {target_dir}")
                    
                    elif "Turkei" in fname:
                        new_file_path = os.path.join(target_dir, fname.replace("Turkei", "Turkey"))
                        
                        shutil.copy2(file_path, new_file_path)
                        print(f"Created a copy of {fname} as Turkey in {target_dir}")

                    elif "Taiwan" in fname:
                        new_file_path_1 = os.path.join(target_dir, fname.replace("Taiwan", "Taiwan"))
                        new_file_path_2 = os.path.join(target_dir, fname.replace("Taiwan", "Taiwan Region"))
                        
                        shutil.copy2(file_path, new_file_path_1)
                        shutil.copy2(file_path, new_file_path_2)
                        print(f"Created copies of {fname} as Taiwan and Taiwan Region in {target_dir}")
                        
    except Exception as e:
        print("An error occurred:", str(e))

copy_and_rename_files(src, trg1, trg2)
