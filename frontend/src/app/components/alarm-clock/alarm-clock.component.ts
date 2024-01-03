import { Component } from '@angular/core';
import { SnackbarService } from 'src/app/services/snackbar.service';
@Component({
  selector: 'app-alarm-clock',
  templateUrl: './alarm-clock.component.html',
  styleUrls: ['./alarm-clock.component.css']
})
export class AlarmClockComponent {

  constructor(private snackBar:SnackbarService) {}
  selectedTime: string = '';
  onTimeSet(event: any) {
    console.log('Selected time:', event);
    this.selectedTime = event
    
    
  }
  onSetAlarmClick() {
    this.snackBar.showSnackBar('Alarm set at: '+ this.selectedTime, "Ok");
  }

}
