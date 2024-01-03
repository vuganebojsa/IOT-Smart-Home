import { Component, Input, OnInit } from '@angular/core';
import { SmarthomeService } from 'src/app/services/smarthome.service';

@Component({
  selector: 'app-device-info',
  templateUrl: './device-info.component.html',
  styleUrls: ['./device-info.component.css']
})
export class DeviceInfoComponent implements OnInit{
  @Input() deviceName = '';
  @Input() measurementName = '';
  constructor(private service: SmarthomeService){}

  ngOnInit(): void {
    this.service.get_last_measurement(this.measurementName, this.deviceName).subscribe(
      result =>{
        console.log(result);
      }
    )
  }
}
