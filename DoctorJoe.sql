create table device
(
    device_id      int          not null
        primary key,
    device_name    varchar(255) null,
    device_version varchar(255) null,
    vendor_id      int          null,
    description    varchar(999) null,
    picture        varchar(255) null,
    constraint fk_vendor
        foreign key (vendor_id) references vendor (vendor_id)
);

INSERT INTO DoctorJoe.device (device_id, device_name, device_version, vendor_id, description, picture) VALUES (0, 'Nuance Power MIC III', '0.0.0', 0, 'Designed to enhance productivity and provide ergonomic control of both standard dictation and speech recognition functions.', 'mic.jpg');

create table driver
(
    device_id     int          not null,
    os_name       varchar(255) null,
    client_driver varchar(255) null,
    agent_driver  varchar(255) null,
    id            int auto_increment
        primary key
);

INSERT INTO DoctorJoe.driver (device_id, os_name, client_driver, agent_driver, id) VALUES (0, 'Windows', 'xxx-0', 'xxx-1', 2);

create table matrix
(
    device_id              int          not null,
    client_os_name         varchar(255) null,
    Horizon_client_version varchar(255) null,
    agent_os_name          varchar(255) null,
    Horizon_agent_version  varchar(255) null,
    redirect_method        varchar(255) null,
    id                     int auto_increment
        primary key
);

INSERT INTO DoctorJoe.matrix (device_id, client_os_name, Horizon_client_version, agent_os_name, Horizon_agent_version, redirect_method, id) VALUES (0, 'Windows 10', '1.2.4', 'Windows Server 2016', '1.2.6', 'direct', 1);

create table vendor
(
    vendor_id   int          not null
        primary key,
    vendor_name varchar(255) null,
    vendor_logo varchar(255) null,
    vendor_link varchar(255) null
);

INSERT INTO DoctorJoe.vendor (vendor_id, vendor_name, vendor_logo, vendor_link) VALUES (0, 'Nuance', 'nuance.jpg', 'https://www.nuance.com');