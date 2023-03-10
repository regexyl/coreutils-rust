# GNU Coreutils Rust translations

Files from GNU coreutils are translated to Rust using `c2rust` from the `src` directory.

To generate the Clippy output for each file, run the following command with each file individually:
```sh
rustc --cfg=clippy <file_name>.rs >> clippy_output/clippy_<file_name>.txt 2>&1
```
* If you don't include `2>&1` in the output redirection command, the stderr output of the rustc command will not be redirected to the output file. Instead, it will be displayed in the terminal as usual.