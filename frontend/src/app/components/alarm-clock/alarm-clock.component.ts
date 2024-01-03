import { Component } from '@angular/core';
import { SnackbarService } from 'src/app/services/snackbar.service';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-alarm-clock',
  templateUrl: './alarm-clock.component.html',
  styleUrls: ['./alarm-clock.component.css']
})
export class AlarmClockComponent {

  constructor(private snackBar:SnackbarService, private httpClient: HttpClient) {}
  selectedTime: string = '';
  onTimeSet(event: any) {
    console.log('Selected time:', event);
    this.selectedTime = event
    
    
  }
  onSetAlarmClick() {
    const alarmTime = this.selectedTime;
  
    // Postavite URL vašeg Flask servera
    const apiUrl = 'http://localhost:5000/set_alarm';
  
    // Napravite JSON objekat koji sadrži vreme alarma
    const requestData = { alarm_time: alarmTime };
  
    // Pošaljite POST zahtev ka Flask serveru
    this.httpClient.post(apiUrl, requestData).subscribe(
      (response) => {
        console.log('Server response:', response);
        this.snackBar.showSnackBar('Alarm set at: ' + this.selectedTime, 'Ok');
      },
      (error) => {
        console.error('Error:', error);
        this.snackBar.showSnackBar('Error setting alarm', 'Ok');
      }
    );
  }

}
