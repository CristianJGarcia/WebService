#!/bin/bash

#Write Curl commands here (10)

CHECK1=0
CHECK2=0
CHECK3=0
CHECK4=0
CHECK5=0
CHECK6=0
CHECK7=0
CHECK8=0
CHECK9=0
CHECK10=0
CHECK11=0

python3 ./web.py &

last_pid=$!

sleep 2

rm -Rf actual.txt

#/hello
curl --silent -X GET "http://52.170.167.62:12075/hello" -H "accept: */*" > actual.txt
if grep "{\"message\":\"hello yourself\"}" actual.txt; then

    CHECK1=1

else

    CHECK1=0

fi

#/properties
curl --silent -IX GET "http://52.170.167.62:12075/properties" > actual.txt
if grep "HTTP/1.0 200 OK" actual.txt; then

    CHECK2=1

else

    CHECK2=0

fi
#https/properties
#curl --insecure --silent -IX GET "https://cs47832.fulgentcorp.com:12070/properties" > actual.txt
#if grep "HTTP/1.0 200 OK" actual.txt; then

 #   CHECK3=1

#else

 #   CHECK3=0

#fi

#/properties/id add
curl --silent -d '{"address":"1015 W 4th st", "city":"weslaco", "id":-1,"state":"TX","zip":"78596"}' -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X POST "http://52.170.167.62:12075/properties" > actual.txt
if grep "{\"message\":\"added\"}" actual.txt; then

    CHECK4=1
    ID=`curl --silent -X GET "http://52.170.167.62:12075/properties" | grep -Po "(\d*),\"\w*\":\"\w*\",\"\w*\":\"\d*\"}]?$" | sed -E 's/(^[0-9]+).*/\1/g'`

else

    CHECK4=0

fi

#/properties view
curl --silent -IX GET "http://52.170.167.62:12075/properties/$ID" > actual.txt
if grep "HTTP/1.0 200 OK" actual.txt; then

    CHECK5=1

else

    CHECK5=0

fi

#/properties update
curl --silent -d '{"address":"test", "city":"test", "id":-1,"state":"CA","zip":"test"}' -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X PUT "http://52.170.167.62:12075/properties/$ID" > actual.txt
if grep "{\"message\":\"updated\"}" actual.txt; then

    CHECK6=1

else

    CHECK6=0

fi

#/properties delete
curl --silent -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X DELETE "http://52.170.167.62:12075/properties/$ID" > actual.txt
if grep "{\"message\":\"deleted\"}" actual.txt; then

    CHECK7=1

else

    CHECK7=0

fi

#https functionality tests here
#https/properties/id add
#curl --silent --insecure -d '{"address":"1015 W 4th st", "city":"weslaco", "id":-1,"state":"TX","zip":"78596"}' -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X POST "https://cs47832.fulgentcorp.com:12070/properties" > actual.txt
#if grep "{\"message\":\"added\"}" actual.txt; then

 #   CHECK8=1
  #  ID=`curl --silent --insecure -X GET "https://cs47832.fulgentcorp.com:12070/properties" | grep -Po "(\d*),\"\w*\":\"\w*\",\"\w*\":\"\d*\"}]?$" | sed -E 's/(^[0-9]+).*/\1/g'`

#else

 #   CHECK8=0

#fi

#https/properties view
#curl --silent --insecure -IX GET "https://cs47832.fulgentcorp.com:12070/properties/$ID" > actual.txt
#if grep "HTTP/1.0 200 OK" actual.txt; then

 #   CHECK9=1

#else

 #   CHECK9=0

#fi

#https/properties update
#curl --silent --insecure -d '{"address":"test", "city":"test", "id":-1,"state":"CA","zip":"test"}' -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X PUT "https://cs47832.fulgentcorp.com:12070/properties/$ID" > actual.txt
#if grep "{\"message\":\"updated\"}" actual.txt; then

 #   CHECK10=1

#else

 #   CHECK10=0

#fi

#https/properties delete
#curl --silent --insecure -H "Content-Type: application/json" -H "Authorization: cs4783FTW" -X DELETE "https://cs47832.fulgentcorp.com:12070/properties/$ID" > actual.txt
#if grep "{\"message\":\"deleted\"}" actual.txt; then

 #   CHECK11=1

#else

 #   CHECK11=0

#fi

if [ $CHECK1 = 0 ]; then

    echo "CURL TEST ERROR: /hello failed"

    kill -KILL $last_pid

    exit 1

fi

if [ $CHECK2 = 0 ]; then

    echo "CURL TEST ERROR: http/properties failed"

    kill -KILL $last_pid

    exit 1

fi

#if [ $CHECK3 = 0 ]; then

 #   echo "CURL TEST ERROR: https/properties failed"

  #  kill -KILL $last_pid

   # exit 1

#fi

if [ $CHECK4 = 0 ]; then

    echo "CURL TEST ERROR: http/properties add failed"

    kill -KILL $last_pid

    exit 1

fi

if [ $CHECK5 = 0 ]; then

    echo "CURL TEST ERROR: http/properties/id view by id failed"

    kill -KILL $last_pid

    exit 1

fi

if [ $CHECK6 = 0 ]; then

    echo "CURL TEST ERROR: http/properties/id update by id failed"

    kill -KILL $last_pid

    exit 1

fi

if [ $CHECK7 = 0 ]; then

    echo "CURL TEST ERROR: http/properties/id delete by id failed"

    kill -KILL $last_pid

    exit 1

fi

#if [ $CHECK8 = 0 ]; then

 #   echo "CURL TEST ERROR: https/properties/id add failed"

  #  kill -KILL $last_pid

   # exit 1

#fi

#if [ $CHECK9 = 0 ]; then

 #   echo "CURL TEST ERROR: https/properties/id view failed"

  #  kill -KILL $last_pid

   # exit 1

#fi

#if [ $CHECK10 = 0 ]; then

 #   echo "CURL TEST ERROR: https/properties/id update failed"

  #  kill -KILL $last_pid

   # exit 1

#fi

#if [ $CHECK11 = 0 ]; then

 #   echo "CURL TEST ERROR: https/properties/id delete failed"

  #  kill -KILL $last_pid

   # exit 1

#fi

echo "CURL TESTS SUCCESS"

kill -KILL $last_pid

exit 0