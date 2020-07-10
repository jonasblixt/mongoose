EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A2 23386 16535
encoding utf-8
Sheet 2 4
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	3750 1950 3100 1950
Wire Wire Line
	3750 2050 3100 2050
Wire Wire Line
	3750 2150 3100 2150
Wire Wire Line
	3750 2250 3100 2250
Wire Wire Line
	3750 2350 3100 2350
Wire Wire Line
	3750 2450 3100 2450
Wire Wire Line
	3750 2550 3100 2550
Wire Wire Line
	3750 2650 3100 2650
Wire Wire Line
	3750 2850 3100 2850
Wire Wire Line
	3750 2950 3100 2950
Wire Wire Line
	3750 3050 3100 3050
Wire Wire Line
	3750 3150 3100 3150
Text Label 3100 1950 0    50   ~ 0
EMMC_D0
Text Label 3100 2050 0    50   ~ 0
EMMC_D1
Text Label 3100 2150 0    50   ~ 0
EMMC_D2
Text Label 3100 2250 0    50   ~ 0
EMMC_D3
Text Label 3100 2350 0    50   ~ 0
EMMC_D4
Text Label 3100 2450 0    50   ~ 0
EMMC_D5
Text Label 3100 2550 0    50   ~ 0
EMMC_D6
Text Label 3100 2650 0    50   ~ 0
EMMC_D7
Text Label 3100 2850 0    50   ~ 0
EMMC_CMD
Text Label 3100 2950 0    50   ~ 0
EMMC_CLK
Text Label 3100 3050 0    50   ~ 0
EMMC_STROBE
Text Label 3100 3150 0    50   ~ 0
EMMC_RESET_N
Wire Wire Line
	6400 7350 7150 7350
Wire Wire Line
	6400 7450 7150 7450
Wire Wire Line
	6400 7700 7150 7700
Wire Wire Line
	6400 7800 7150 7800
Wire Wire Line
	6400 7900 7150 7900
Wire Wire Line
	6400 8000 7150 8000
Wire Wire Line
	6400 8200 7150 8200
Wire Wire Line
	6400 8300 7150 8300
Wire Wire Line
	6400 8500 7150 8500
Wire Wire Line
	6400 8600 7150 8600
Wire Wire Line
	6400 8700 7150 8700
Wire Wire Line
	6400 8800 7150 8800
Wire Wire Line
	6400 9000 7150 9000
Wire Wire Line
	6400 9100 7150 9100
Text Label 7150 7350 2    50   ~ 0
ENET_TX_CTL
Text Label 7150 7450 2    50   ~ 0
ENET_TXC
Text Label 7150 7700 2    50   ~ 0
ENET_RD0
Text Label 7150 7800 2    50   ~ 0
ENET_RD1
Text Label 7150 7900 2    50   ~ 0
ENET_RD2
Text Label 7150 8000 2    50   ~ 0
ENET_RD3
Text Label 7150 8200 2    50   ~ 0
ENET_RXC
Text Label 7150 8300 2    50   ~ 0
ENET_RX_CTL
Text Label 7150 8500 2    50   ~ 0
ENET_TD0
Text Label 7150 8600 2    50   ~ 0
ENET_TD1
Text Label 7150 8700 2    50   ~ 0
ENET_TD2
Text Label 7150 8800 2    50   ~ 0
ENET_TD3
Text Label 7150 9000 2    50   ~ 0
ENET_MDC
Text Label 7150 9100 2    50   ~ 0
ENET_MDIO
$Comp
L cpu:MIMX8MN5DVTJZAA U1
U 1 1 5EEF14F0
P 3950 15100
F 0 "U1" H 5075 28865 50  0000 C CNN
F 1 "MIMX8MN5DVTJZAA" H 5075 28774 50  0000 C CNN
F 2 "BGA-486_27x27_P0.5mm_14.0x14.0mm" H 4750 14600 50  0001 C CNN
F 3 "" H 3450 15700 50  0001 C CNN
F 4 "NXP" H 4550 14850 50  0001 C CNN "Manufacturer"
F 5 "MIMX8MN5DVTJZAA" H 4600 14750 50  0001 C CNN "Part Number"
	1    3950 15100
	1    0    0    -1  
$EndComp
$Sheet
S 20150 3000 1900 1350
U 5F6FEC58
F0 "DRAM" 50
F1 "dram.sch" 50
$EndSheet
$Sheet
S 20150 1300 1900 1400
U 5F847585
F0 "Power" 50
F1 "power.sch" 50
$EndSheet
Text Notes 10350 1700 0    118  ~ 24
Review IMX pin-out
$EndSCHEMATC
