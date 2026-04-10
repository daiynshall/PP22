DROP PROCEDURE IF EXISTS insert_many_contacts(TEXT[], TEXT[]);

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]{11}$' THEN

            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = names[i]) THEN
                UPDATE phonebook
                SET phone_number = phones[i]
                WHERE first_name = names[i]
                  AND NOT EXISTS (
                      SELECT 1
                      FROM phonebook
                      WHERE phone_number = phones[i]
                        AND first_name <> names[i]
                  );

                IF NOT FOUND THEN
                    RAISE NOTICE 'Skipped duplicate phone: %, name: %', phones[i], names[i];
                END IF;

            ELSIF EXISTS (SELECT 1 FROM phonebook WHERE phone_number = phones[i]) THEN
                RAISE NOTICE 'Skipped duplicate phone: %, name: %', phones[i], names[i];

            ELSE
                INSERT INTO phonebook(first_name, phone_number)
                VALUES (names[i], phones[i]);
            END IF;

        ELSE
            RAISE NOTICE 'Invalid phone: %, name: %', phones[i], names[i];
        END IF;
    END LOOP;
END;
$$;