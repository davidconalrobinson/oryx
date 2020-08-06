docker run --name oryx ^
    -e HOSTNAME=oryx ^
    -e POSTGRES_PASSWORD=postgres ^
    -e POSTGRES_USER=postgres ^
    -e POSTGRES_DB=oryx ^
    -p 5432:5432 ^
    -d postgres
pause