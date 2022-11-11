CREATE TABLE public."PHONEBOOK"
(
   id integer NOT NULL,
   name_ text COLLATE pg_catalog."default" NOT NULL,
   phone_number char(12) COLLATE pg_catalog."default" NOT NULL
)
TABLESPACE pg_default;
ALTER TABLE public."PHONEBOOK"
   OWNER to postgres;


INSERT INTO public."PHONEBOOK"( id, name_, phone_number)
VALUES (1, 'test 1', '02199999999');

SELECT * FROM public."PHONEBOOK