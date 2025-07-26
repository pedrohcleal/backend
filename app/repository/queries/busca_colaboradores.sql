WITH users_cte AS (
    SELECT
        us.id,
        us.nome_completo,
        us.id_dp,
        COUNT(deps.id) > 0 AS have_dependents
    FROM users AS us
    LEFT JOIN dependentes AS deps ON us.id = deps.id_user
    GROUP BY us.id, us.nome_completo, us.id_dp
)
SELECT
    us.nome_completo,
    us.have_dependents
FROM users_cte AS us
INNER JOIN departamentos AS deps ON us.id_dp = deps.id
WHERE deps.id = :departamento_id;
