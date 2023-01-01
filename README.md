# aster-wallpaper-template

### You can use this script to download images from nasa api daily using github actions
### to configure change folliging USERNAME
            >  git config --global user.name 'USERNAME'
            >  git config --global user.email 'USERNAME@users.noreply.github.com'
###      to approriate values
   
   
## To chane time this script runs change cron value 
            on:
              schedule:
               - cron: "0 2 * * *"
              workflow_dispatch:
For more information visit --> https://crontab.guru


