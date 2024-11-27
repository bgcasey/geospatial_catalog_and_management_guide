# set directory to clone GEE git into (should be empty)
cd ...

# delete all .js files in directory
rm *.js

# clone gee scripts
git clone https://earthengine.googlesource.com/users/username/project_name

# delete .git folder
rm -r project_name/

# add the .js file extention to files
find cproject_name -type f -not -name "*.*" -exec mv "{}" "{}".js \;

# move .js files up a directory
mv -v project_name/*.js .

# delete now empty gee git folder
rmdir project_name

