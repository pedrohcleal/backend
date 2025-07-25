WITH users_cte as(
    SELECT
        us.nome_completo,
        CASE
            WHEN deps.id is NULL THEN FALSE
            ELSE TRUE
        END AS have_dependents,
        us.id_dp
    FROM users AS us
    FULL JOIN dependentes AS deps ON us.id = deps.id_user
    GROUP BY us.nome_completo
    ORDER BY nome_completo ASC
)
SELECT
    us.nome_completo,
    us.have_dependents
FROM users_cte AS us
INNER JOIN departamentos AS deps ON us.id_dp = deps.id
WHERE deps.id = :departamento_id
