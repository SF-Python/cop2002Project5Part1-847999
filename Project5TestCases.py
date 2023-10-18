import unittest

#Cannot have spaces in filenames to be imported
from project5 import *

class TestGenerateTestCase(unittest.TestCase):
    def setUp(self):
        self.portNum=["20", "21", "22", "23", "25", "53", "67", "68", "80", "110",
                 "137", "139", "143", "161", "162", "389", "443", "445", "3389"]

        self.portName=["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP",
                  "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS",
                  "SMB", "RDP"]

    ############ Testing Port Numbers ############

    # Must start test cases with keyword "test_"
    def test_port20(self):
        """Port 20"""

        index=0

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])
        

    def test_port21(self):
        """Port 21"""
        index=1

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port22(self):
        """Port 22"""
        index=2

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port23(self):
        """Port 23"""
        index=3

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port25(self):
        """Port 25"""
        index=4

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port53(self):
        """Port 53"""
        index=5

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port67(self):
        """Port 67"""
        index=6

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port68(self):
        """Port 68"""
        index=7

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port80(self):
        """Port 80"""
        index=8

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port110(self):
        """Port 110"""
        index=9

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port137(self):
        """Port 137"""
        index=10

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port139(self):
        """Port 139"""
        index=11

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port143(self):
        """Port 143"""
        index=12

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port161(self):
        """Port 161"""
        index=13

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port162(self):
        """Port 162"""
        index=14

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port389(self):
        """Port 389"""
        index=15

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port443(self):
        """Port 443"""
        index=16

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port445(self):
        """Port 445"""
        index=17

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    def test_port3389(self):
        """Port 3389"""
        index=18

        self.assertEqual(numToName(self.portNum, self.portName, self.portNum[index]), self.portName[index])

    ############ Testing Port Names ############

    # Must start test cases with keyword "test_"
    def test_portFTP20(self):
        """Port 20 """

        index=0

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        FTPArray=["20", "21"] # required array for FTP

        answer=True

        if(len(programAnswerArray) != len(FTPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != FTPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)

    def test_portFTP21(self):
        """Port 21 """

        index=1

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        FTPArray=["20", "21"] # required array for FTP

        answer=True

        if(len(programAnswerArray) != len(FTPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != FTPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)


    def test_portSSH22(self):
        """Port 22"""
        index=2

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
        
    def test_portTelnet23(self):
        """Port 23"""
        index=3

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
        
    def test_portSMTP25(self):
        """Port 25"""
        index=4

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
        
    def test_portDNS53(self):
        """Port 53"""
        index=5

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 
    def test_portDHCP67(self):
        """Port 67"""
        index=6
        
        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        DHCPArray=["67", "68"] # required array for DHCP

        answer=True

        if(len(programAnswerArray) != len(DHCPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != DHCPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
 
    def test_portDHCP68(self):
        """Port 68"""
        index=7

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        DHCPArray=["67", "68"] # required array for DHCP

        answer=True

        if(len(programAnswerArray) != len(DHCPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != DHCPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
        
    def test_portHTTP80(self):
        """Port 80"""
        index=8

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 
    def test_portPOP3_110(self):
        """Port 110"""
        index=9

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 
    def test_portNetBIOS_137(self):
        """Port 137"""
        index=10

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        NetBIOSArray=["137", "139"] # required array for NetBIOS

        answer=True

        if(len(programAnswerArray) != len(NetBIOSArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != NetBIOSArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
 
    def test_portNetBIOS_139(self):
        """Port 139"""
        index=11

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        NetBIOSArray=["137", "139"] # required array for NetBIOS

        answer=True

        if(len(programAnswerArray) != len(NetBIOSArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != NetBIOSArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
        
    def test_portIMAP143(self):
        """Port 143"""
        index=12

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 
    def test_portSNMP_161(self):
        """Port 161"""
        index=13

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        SNMPArray=["161", "162"] # required array for SNMP

        answer=True

        if(len(programAnswerArray) != len(SNMPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != SNMPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
 
    def test_portSNMP_162(self):
        """Port 162"""
        index=14

        programAnswerArray=nameToNum(self.portNum, self.portName, self.portName[index]) # get array from program
        programAnswerArray.sort() # sort the list

        SNMPArray=["161", "162"] # required array for SNMP

        answer=True

        if(len(programAnswerArray) != len(SNMPArray)):  # if different lengths, then not correct
            answer=False
        else:
            for i in range(len(programAnswerArray)):
                if(programAnswerArray[i] != SNMPArray[i]):  # if different value in a position, not correct
                    answer=False

        self.assertTrue(answer)
        
    def test_portLDAP389(self):
        """Port 389"""
        index=15

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 
    def test_portHTTPS443(self):
        """Port 443"""
        index=16

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
        
    def test_portSMB445(self):
        """Port 445"""
        index=17

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
        
    def test_portRDP3389(self):
        """Port 3389"""
        index=18

        answer=nameToNum(self.portNum, self.portName, self.portName[index])

        self.assertEqual(answer[0], self.portNum[index])
 

if __name__ == '__main__':
    unittest.main()
