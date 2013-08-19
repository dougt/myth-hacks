FRONTENDS=(mythfe@192.168.1.101 mythfe@192.168.1.103)

# Frontend 
#  We --force-architecture during installation of debs because one
#  of the frontends is a AMD64 and we are building 32 bits
# 
#  This script should run without prompt if the users have sudo
#  access without password (see sudo visudo).

index=0
element_count=${#FRONTENDS[@]}
while [ "$index" -lt "$element_count" ]
do
    current=${FRONTENDS[$index]}

    echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    ssh $current sudo reboot
    echo "Rebooting "$current

    ((index++))
done

echo "All done."
