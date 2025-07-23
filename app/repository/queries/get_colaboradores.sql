SELECT
    us.nome_completo,
    CASE
        WHEN deps.id is NULL THEN FALSE
        ELSE TRUE
    END AS have_dependents
FROM users AS us
FULL JOIN dependentes AS deps ON us.id = deps.id_user
GROUP BY us.nome_completo
ORDER BY nome_completo ASC
