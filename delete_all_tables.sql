-- drop table if exists auth_group;
-- drop table if exists auth_group_permissions;
-- drop table if exists auth_permission;
-- drop table if exists authentication_user;
-- drop table if exists authentication_user_groups;
-- drop table if exists authentication_user_user_permissions;

-- alter table oauth2_provider_accesstoken drop constraint if exists oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr;
-- alter table oauth2_provider_refreshtoken drop constraint if exists oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr;
-- alter table oauth2_provider_refreshtoken drop constraint if exists oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr;
-- drop table if exists oauth2_provider_accesstoken;
-- drop table if exists oauth2_provider_refreshtoken;
-- drop table if exists oauth2_provider_application;

-- alter table authtoken_token drop constraint if exists authtoken_token_user_id_35299eff_fk_auth_user_id;
-- drop table if exists authtoken_token;
-- alter table django_admin_log drop constraint if exists django_admin_log_user_id_c564eba6_fk_auth_user_id;
-- drop table if exists django_admin_log;
-- drop table if exists auth_user;

-- drop table if exists django_migrations;
-- drop table if exists django_content_type;
-- drop table if exists django_session;

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
