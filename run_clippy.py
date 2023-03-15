import os

src_dir = "src/"
output_dir = "src/clippy_output/"

rs_files = [f for f in os.listdir(src_dir) if f.endswith(".rs")]

for rs_file in rs_files:
    # Extract the file name without the extension
    file_name = os.path.splitext(rs_file)[0]
    command = f"rustc --cfg=clippy {src_dir}/{rs_file} > {output_dir}/clippy_{file_name}.txt 2>&1"
    os.system(command)
