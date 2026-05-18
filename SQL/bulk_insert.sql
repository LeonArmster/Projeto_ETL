BULK INSERT {tabela}
FROM '{arquivo}'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    TABLOCK
)