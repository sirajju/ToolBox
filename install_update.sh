echo ("Installing update..")
mv Cryptography.py setup.bat version.txt README.txt -r ..
cd ..
rmdir --ignore-fail-on-non-empty Cryptography 

echo "Updated to latest version.."