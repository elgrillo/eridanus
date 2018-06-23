import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/from';
import { Weighing } from './weighing.model';

@Injectable()
export class WeighingService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Weighing> {
    return Observable.from([
      {
        id: '1',
        weight: 100.0,
        weighingDate: new Date(2018, 4, 6)
      },
      {
        id: '2',
        weight: 103.0,
        weighingDate: new Date(2018, 4, 9)
      }
    ]);

    // return this.http.get('//localhost:8080/api/weighings');
  }

}
