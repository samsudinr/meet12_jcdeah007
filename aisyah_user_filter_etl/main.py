from extract import extract_usernames_from_folder
from transform import filter_difference
from load import save_csv, save_txt

folder_not_verify = "mixed_not_verify_bpjs"
folder_verify = "mixed_verify_bpjs"

output_combined_not_verify = "combined_username.csv"
output_combined_verify = "combined_username_bpjs.csv"
output_difference_txt = "clean_non_verify_bpjs_usernames.txt"

usernames_not_verify = extract_usernames_from_folder(folder_not_verify)
usernames_verify = extract_usernames_from_folder(folder_verify)

save_csv(usernames_not_verify, output_combined_not_verify)
save_csv(usernames_verify, output_combined_verify)

difference = filter_difference(usernames_not_verify, usernames_verify)

save_txt(difference, output_difference_txt)

print(f"✅ ETL pipeline finished. Result saved to {output_difference_txt}")
