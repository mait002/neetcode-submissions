-- Write your query below
SELECT e.left_operand, e.operator, e.right_operand,
CASE
    WHEN e.operator = '>' AND a.value > b.value THEN 'true'
    WHEN e.operator = '<' AND a.value < b.value THEN 'true'
    WHEN e.operator = '=' AND a.value = b.value THEN 'true'
    ELSE 'false'
END AS value
FROM expressions e
JOIN variables a ON e.left_operand = a.name
JOIN variables b ON e.right_operand = b.name;
