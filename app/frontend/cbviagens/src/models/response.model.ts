export interface ResponseModel<T>{
    status: string,
    code: number,
    data: T
}