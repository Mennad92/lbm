BEGIN;
--
-- Create model UserData
--
CREATE TABLE "biscuits_userdata" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(100) NOT NULL UNIQUE, "address" varchar(100) NOT NULL, "city" varchar(100) NOT NULL, "country" varchar(100) NOT NULL, "phone" varchar(20) NULL, "postal" varchar(10) NULL, "date_joined" datetime NOT NULL, "is_admin" bool NOT NULL, "is_active" bool NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL);
CREATE TABLE "biscuits_userdata_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "userdata_id" bigint NOT NULL REFERENCES "biscuits_userdata" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "biscuits_userdata_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "userdata_id" bigint NOT NULL REFERENCES "biscuits_userdata" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Category
--
CREATE TABLE "biscuits_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(70) NOT NULL);
--
-- Create model Ingredient
--
CREATE TABLE "biscuits_ingredient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Order
--
CREATE TABLE "biscuits_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "uuid" varchar(50) NOT NULL UNIQUE, "status" varchar(50) NOT NULL, "owner_id" bigint NOT NULL REFERENCES "biscuits_userdata" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ProductData
--
--
-- Create model Product
--
CREATE TABLE "biscuits_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(70) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "stock" integer unsigned NOT NULL CHECK ("stock" >= 0), "illustration" varchar(100) NOT NULL, "category_id" bigint NOT NULL REFERENCES "biscuits_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "biscuits_product_ingredients" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_id" bigint NOT NULL REFERENCES "biscuits_product" ("id") DEFERRABLE INITIALLY DEFERRED, "ingredient_id" bigint NOT NULL REFERENCES "biscuits_ingredient" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model OrderElement
--
CREATE TABLE "biscuits_orderelement" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer unsigned NOT NULL CHECK ("quantity" >= 0), "product_id" bigint NOT NULL REFERENCES "biscuits_product" ("id") DEFERRABLE INITIALLY DEFERRED, "related_order_id" bigint NOT NULL REFERENCES "biscuits_order" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "biscuits_userdata_groups_userdata_id_group_id_01326e4c_uniq" ON "biscuits_userdata_groups" ("userdata_id", "group_id");
CREATE INDEX "biscuits_userdata_groups_userdata_id_ad6d2e90" ON "biscuits_userdata_groups" ("userdata_id");
CREATE INDEX "biscuits_userdata_groups_group_id_a3d95de0" ON "biscuits_userdata_groups" ("group_id");
CREATE UNIQUE INDEX "biscuits_userdata_user_permissions_userdata_id_permission_id_3773f52b_uniq" ON "biscuits_userdata_user_permissions" ("userdata_id", "permission_id");
CREATE INDEX "biscuits_userdata_user_permissions_userdata_id_4a25822e" ON "biscuits_userdata_user_permissions" ("userdata_id");
CREATE INDEX "biscuits_userdata_user_permissions_permission_id_c7ed7377" ON "biscuits_userdata_user_permissions" ("permission_id");
CREATE INDEX "biscuits_order_owner_id_d327804f" ON "biscuits_order" ("owner_id");
CREATE INDEX "biscuits_product_category_id_fc313a6d" ON "biscuits_product" ("category_id");
CREATE UNIQUE INDEX "biscuits_product_ingredients_product_id_ingredient_id_19ed9405_uniq" ON "biscuits_product_ingredients" ("product_id", "ingredient_id");
CREATE INDEX "biscuits_product_ingredients_product_id_54830f7e" ON "biscuits_product_ingredients" ("product_id");
CREATE INDEX "biscuits_product_ingredients_ingredient_id_e8dc64be" ON "biscuits_product_ingredients" ("ingredient_id");
CREATE INDEX "biscuits_orderelement_product_id_7358624c" ON "biscuits_orderelement" ("product_id");
CREATE INDEX "biscuits_orderelement_related_order_id_f60a058a" ON "biscuits_orderelement" ("related_order_id");
COMMIT;
