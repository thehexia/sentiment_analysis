folder=$1;

mkdir $folder"by_day" 2> /dev/null
output=$folder"by_day/"

day[0]="10-06-2014";
day[1]="10-07-2014";
day[2]="10-08-2014";
day[3]="10-09-2014";
day[4]="10-10-2014";
day[5]="10-11-2014";
day[6]="10-12-2014";
day[7]="10-13-2014";
day[8]="10-14-2014";
day[9]="10-15-2014";
day[10]="10-16-2014";
day[11]="10-17-2014";
day[12]="10-18-2014";
day[13]="10-19-2014";
day[14]="10-20-2014";
day[15]="10-21-2014";
day[16]="10-22-2014";
day[17]="10-23-2014";
day[18]="10-24-2014";
day[19]="10-25-2014";
day[20]="10-26-2014";
day[21]="10-27-2014";
day[22]="10-28-2014";
day[23]="10-29-2014";
day[24]="10-30-2014";
day[25]="10-31-2014";
day[26]="11-01-2014";
day[27]="11-02-2014";
day[28]="11-03-2014";
day[29]="11-04-2014";
day[30]="11-05-2014";
day[31]="11-06-2014";

for days in ${day[@]};
do
	mkdir $output$days 2> /dev/null;
	echo $days;
	cp  $(ls $folder | grep $days | awk -v o=$folder '{print o$1}') $output$days;
done


