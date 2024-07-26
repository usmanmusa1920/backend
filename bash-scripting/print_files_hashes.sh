#!/bin/sh
# This shell script computes and prints the MD5, SHA1, and SHA256 hashes for all files in the current directory and its subdirectories, excluding files named Release.

# Shebang Line (#!/bin/sh) indicates that the script should be executed using the sh shell.

# This command ensures that the script will exit immediately if any command exits with a non-zero status.
set -e

do_hash() {
    # The function takes two parameters: `HASH_NAME` and `HASH_CMD`.

    # The name of the hash function (e.g., "MD5Sum")
    HASH_NAME=$1

    # The command used to compute the hash (e.g., md5sum)
    HASH_CMD=$2

    echo "${HASH_NAME}:"

    for f in $(find -type f); do
        f=$(echo $f | cut -c3-) # remove ./ prefix

        if [ "$f" = "Release" ]; then
            continue
        fi

        echo " $(${HASH_CMD} ${f}  | cut -d" " -f1) $(wc -c $f)"
    done
}

# cat << EOF
# Origin: Example Repository
# Label: Example
# Suite: stable
# Codename: stable
# Version: 1.0
# Architectures: amd64 arm64 arm7
# Components: main
# Description: An example software repository
# Date: $(date -Ru)
# EOF

do_hash "MD5Sum" "md5sum"
do_hash "SHA1" "sha1sum"
do_hash "SHA256" "sha256sum"

# Overall, the script outputs the hash values and sizes of all files in the current directory and its subdirectories for each specified hash algorithm, excluding files named Release.
