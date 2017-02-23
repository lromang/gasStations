/* Penalizaciones */
drop table if exists gas cascade;

create table gas (
        id int,
        date date,
        lat numeric,
        lon numeric,
        price numeric,
        time time,
        type varchar(30)
        );

\copy gas from '/home/luis/Documents/Work/Presidencia/gasStations/data/clean_price.csv' with delimiter as ',' csv;
