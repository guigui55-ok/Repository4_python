
REPLACE_TABLE_NAMES = '___TABLE_NAMES___'
REPLACE_TABLE_NAME = '___TABLE_NAME___'
TABLE_COLUMN_BASIC_INFOS = """SELECT
	t.name                  AS テーブル名,
	c.name                  AS 項目名,
	type_name(user_type_id) AS 属性,
	max_length              AS 長さ,
	CASE
		WHEN
			is_nullable = 1
		THEN
			'YES'
		ELSE
			'NO'
	END AS NULL許可
FROM
	sys.objects t
    INNER JOIN sys.columns c ON
		t.object_id = c.object_id
WHERE
	t.type = 'U'
AND
	t.name IN ___TABLE_NAMES___
ORDER BY
	c.column_id
"""

GET_ALL_INDEX_FROM_DB="""SELECT	S.name AS SchemaName,
	O.name AS ObjectName,
	I.name AS IndexName,
	I.type_desc AS IndexTypeDesc,
	I.is_primary_key AS IsPrimaryKey,
	I.is_unique AS IsUnique,
	I.is_disabled AS IsDisabled
FROM	sys.indexes AS I
	   INNER JOIN sys.objects AS O
	      ON I.object_id = O.object_id
	   INNER JOIN sys.schemas AS S
	      ON O.schema_id = S.schema_id
WHERE	I.index_id > 0
	AND O.is_ms_shipped = 0
ORDER BY S.name,
	 O.name,
	 I.name;
"""
REPLACE_COLUMN_NAME = "___COLUMN_NAME___"
GET_RECORD_COUNT_WITH_COLUMN_NAME = "SELECT COUNT(___COLUMN_NAME___) FROM ___TABLE_NAME___;"

# --件数を取得(列指定なし)
GET_RECORD_COUNT = "SELECT COUNT(*) FROM ___TABLE_NAME___;"

REPLACE_DATE_VALUE = "___DATE_VALUE___"
GET_AFTER_DATE = """SELECT *
FROM ___TABLE_NAME___
WHERE ___COLUMN_NAME___ >= '___DATE_VALUE___';"""

GET_MATCH_VALUE = """SELECT *
FROM ___TABLE_NAME___
WHERE ___TABLE_NAME___.___COLUMN_NAME___ LIKE '___DATE_VALUE___';"""
IS_EXISTS_DATA = GET_MATCH_VALUE
# sql = "SELECT * FROM MainTable WHERE MainTable." + columna_name + " LIKE '{}'".format(url)

REPLACE_SET_COLUMN_NAME = "___SET_COLUMN_NAME___"
REPLACE_SET_DATA_VALUE = "___SET_DATA_VALUE___"
REPLACE_WHRER_COLUMN_NAME = "___WHERE_COLUMN_NAME___"
REPLACE_WHRER_DATA_VALUE = "___WHERE_DATA_VALUE___"

UPDATE_VALUE = """UPDATE ___TABLE_NAME___
SET ___SET_COLUMN_NAME___ = ___SET_DATA_VALUE___
WHERE ___TABLE_NAME___.___WHERE_COLUMN_NAME___ LIKE '___WHERE_DATA_VALUE___'
;"""
# --テーブルの値を更新する
# UPDATE emp
# SET empname = '藤田花子'
# ,address = '神奈川県横浜市1-1-1'
# WHERE empno = 'D001';