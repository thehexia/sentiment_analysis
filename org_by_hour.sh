folder=$1;

mkdir $folder"by_hour" 2> /dev/null
output=$folder"by_hour/"

hour[0]="^.*_..-..-2014_00-..-..$_..";
hour[1]="^.*_..-..-2014_01-..-..$_..";
hour[2]="^.*_..-..-2014_02-..-..$_..";
hour[3]="^.*_..-..-2014_03-..-..$_..";
hour[4]="^.*_..-..-2014_04-..-..$_..";
hour[5]="^.*_..-..-2014_05-..-..$_..";
hour[6]="^.*_..-..-2014_06-..-..$_..";
hour[7]="^.*_..-..-2014_07-..-..$_..";
hour[8]="^.*_..-..-2014_08-..-..$_..";
hour[9]="^.*_..-..-2014_09-..-..$_..";
hour[10]="^.*_..-..-2014_10-..-..$_..";
hour[11]="^.*_..-..-2014_11-..-..$_..";
hour[12]="^.*_..-..-2014_12-..-..$_..";
hour[13]="^.*_..-..-2014_13-..-..$_..";
hour[14]="^.*_..-..-2014_14-..-..$_..";
hour[15]="^.*_..-..-2014_15-..-..$_..";
hour[16]="^.*_..-..-2014_16-..-..$_..";
hour[17]="^.*_..-..-2014_17-..-..$_..";
hour[18]="^.*_..-..-2014_18-..-..$_..";
hour[19]="^.*_..-..-2014_19-..-..$_..";
hour[20]="^.*_..-..-2014_20-..-..$_..";
hour[21]="^.*_..-..-2014_21-..-..$_..";
hour[22]="^.*_..-..-2014_22-..-..$_..";
hour[23]="^.*_..-..-2014_23-..-..$_..";

#ls $folder | grep $hour | awk -v o=$folder '{printf "%s%s\n", o, $1}'

i=0;
for hours in ${hour[@]};
do
	mkdir $output$i 2> /dev/null;
	echo $i
	cp  $(ls $folder | grep $hours | awk -v o=$folder '{print o$1}') $output$i;
	((i=i+1));
done