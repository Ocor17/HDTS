CLASS_CHOICES = [
    ('classified', 'CLASSIFIED'),
    ('unclassified', 'UNCLASSIFIED')
]

CONN_PORT_CHOICES = [
    ('sata', 'SATA'),
    ('m.2', 'M.2')
]

HD_STATUS_CHOICES = [
    ('assigned', 'ASSIGNED'), ('available', 'AVAILABLE'), ('end of life', 'END OF LIFE'), 
    ('master clone', 'MASTER CLONE'), ('pending wipe', 'PENDING WIPE'), ('destroyed', 'DESTROYED'), 
    ('lost', 'LOST'), ('overdue', 'OVERDUE'), ('picked up', 'PICKED UP'), ('returned', 'RETURNED'),
     ('pending classification change', 'PENDING CLASSIFICATION CHANGE')
]

HD_TYPE_CHOICES = [
    ('ssd', 'SSD'),
    ('hdd', 'HDD')
]

HD_MEMORY_SIZES = [
    ('250gb','250GB'),
    ('500gb','500GB'),
    ('750gb','750GB'),
    ('1tb', '1TB')
]

MANUFACTURER_CHOICES = [
    ('toshiba', 'Toshiba'),
    ('seagate', 'Seagate')
]

BOOT_TEST_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No')
]