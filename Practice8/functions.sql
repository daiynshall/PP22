RETURN QUERY
    SELECT p.id, p.first_name, p.phone_number
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern_text || '%'
       OR p.phone_number ILIKE '%' || pattern_text || '%'
    ORDER BY p.id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(contact_id INT, first_name VARCHAR, phone_number VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone_number
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;