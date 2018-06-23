import { TestBed, inject } from '@angular/core/testing';

import { WeighingService } from './weighing.service';

describe('WeighingService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [WeighingService]
    });
  });

  it('should be created', inject([WeighingService], (service: WeighingService) => {
    expect(service).toBeTruthy();
  }));
});
